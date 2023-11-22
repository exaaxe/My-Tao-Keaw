from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1108962695367118890/60Zu5wtmj2wqDc3EnCd3RZNx8zlTE9DxLM3QE-hPj4IZOJs4Un4_ZRlFj10ExZj4Q12A', username="เต่า")

embed = DiscordEmbed(title='Tao', description='I am Turtle', color='3FF942')
embed.set_author(name='August', url='https://cdn.discordapp.com/emojis/833324288646840361.gif?size=96&quality=lossless', icon_url='https://cdn.discordapp.com/emojis/833324288646840361.gif?size=96&quality=lossless')
embed.set_footer(text='I love Tao')
embed.set_timestamp()
embed.add_embed_field(name='เต่า', value='เต่า')
embed.add_embed_field(name='เต่า', value='เต่า')
embed.add_embed_field(name='เต่า', value='เต่า')
embed.add_embed_field(name='เต่า', value='เต่า')
embed.add_embed_field(name='เต่า', value='เต่า')
embed.add_embed_field(name='เต่า', value='เต่า')
embed.add_embed_field(name='เต่า', value='เต่า')
embed.add_embed_field(name='เต่า', value='เต่า')
embed.add_embed_field(name='เต่า', value='เต่า')



webhook.add_embed(embed)
response = webhook.execute()