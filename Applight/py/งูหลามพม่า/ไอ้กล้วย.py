from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1089135994219008050/7KlI5NFfXvi3PEMYcbyWaArG-EB3r5J1fIFG_nshkaP6Jwk5oircCb6Ed-tdp3k9aVxD", username="ฉันคือ กล้วย")

embed = DiscordEmbed(
    title="นายกล้วยน้ำว้า", description="กล้วยตานี", color='ffffff'
)
embed.set_author(
    name="กล้วยไข่",
    url="https://www.youtube.com/watch?v=MKF8pnbsnhw",
    icon_url="https://cdn.discordapp.com/emojis/1013591314199220304.gif?size=96&quality=lossless",
)
embed.set_footer(text="Embed Footer Text")
embed.set_timestamp()
# Set `inline=False` for the embed field to occupy the whole line
embed.add_embed_field(name="กล้วย", value="กล้วยไข่", inline=True)
embed.add_embed_field(name="กล้วย", value="กล้วยแขก", inline=True)


webhook.add_embed(embed)
response = webhook.execute()