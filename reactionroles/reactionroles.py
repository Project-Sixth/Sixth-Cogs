from redbot.core import commands, checks, Config

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, 686868686)
        default_settings = {
            "reactions": []
        }
        self.config.register_guild(**default_settings)
        bot.add_listener(self.on_raw_reaction_add, "on_raw_reaction_add")
        bot.add_listener(self.on_raw_reaction_remove, "on_raw_reaction_remove")
    
    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.bot.user.id:
            return 
        
        executedGuild = [x for x in self.bot.guilds if x.id == payload.guild_id][0]
        allReactions = await self.config.guild(executedGuild).reactions()
        for i in allReactions:
            if i["message_id"] == payload.message_id and i["emoji_id"] == payload.emoji.id:
                executedMember = [x for x in executedGuild.members if x.id == payload.user_id][0]
                changedRole = [x for x in executedGuild.roles if i["role_id"] == x.id][0]
                await executedMember.add_roles(changedRole, reason=f'For adding Emoji ID {payload.emoji.id}')

    async def on_raw_reaction_remove(self, payload):
        if payload.user_id == self.bot.user.id:
            return 
        
        executedGuild = [x for x in self.bot.guilds if x.id == payload.guild_id][0]
        allReactions = await self.config.guild(executedGuild).reactions()
        for i in allReactions:
            if i["message_id"] == payload.message_id and i["emoji_id"] == payload.emoji.id:
                executedMember = [x for x in executedGuild.members if x.id == payload.user_id][0]
                changedRole = [x for x in executedGuild.roles if i["role_id"] == x.id][0]
                await executedMember.remove_roles(changedRole, reason=f'For removing Emoji ID {payload.emoji.id}')
    
    @commands.group()
    @checks.admin()
    async def reactionroles(self, ctx):
        """
        Controller for ReactionRoles
        """
        pass
    
    @reactionroles.command('add')
    async def _add(self, ctx, messageId: int, emoji: commands.PartialEmojiConverter, mentionedRole: commands.RoleConverter):
        """
        Adds a ReactionRole. Takes MessageID, Emoji and MentionedRole.
        Adds Emoji to certain MessageID, and everyone who clicks it receive MentionedRole.
        Also everyone who removes it lose MentionedRole.
        """
        allReactions = await self.config.guild(ctx.guild).reactions()
        allReactions.append({
            "message_id": messageId,
            "emoji_id": emoji.id,
            "role_id": mentionedRole.id
        })
        await self.config.guild(ctx.guild).reactions.set(allReactions)
        msg = await ctx.message.channel.fetch_message(messageId)
        await msg.add_reaction(emoji)
        
    
    @reactionroles.command('remove')
    async def _remove(self, ctx, messageId: int, emoji: commands.PartialEmojiConverter):
        """
        Removes a ReactionRole. Takes MessageID, Emoji.
        Removes certain Emoji from MessageID.
        """
        allReactions = await self.config.guild(ctx.guild).reactions()
        newReactions = []
        for r in allReactions:
            if r["message_id"] == messageId and r["emoji_id"] == emoji.id:
                continue
            newReactions.append(r)
        await self.config.guild(ctx.guild).reactions.set(newReactions)
        msg = await ctx.message.channel.fetch_message(messageId)
        await msg.remove_reaction(emoji, self.bot.user)
    
    @reactionroles.command('list')
    async def _list(self, ctx):
        """
        Lists all active ReactionRoles on the server.
        """
        allReactions = await self.config.guild(ctx.guild).reactions()
        answer = "```Here is all RR active on server:"
        for r in allReactions:
            answer += f'\nEmoji {r["emoji_id"]} on message {r["message_id"]} activates {r["role_id"]}.'
        answer += "```"
        await ctx.send(answer)
    