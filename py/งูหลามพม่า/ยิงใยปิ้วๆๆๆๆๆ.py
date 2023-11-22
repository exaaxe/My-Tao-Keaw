#webhook embed แบบกล่องข้อความ
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1089135994219008050/7KlI5NFfXvi3PEMYcbyWaArG-EB3r5J1fIFG_nshkaP6Jwk5oircCb6Ed-tdp3k9aVxD')

embed = DiscordEmbed(title='Halo', description='I am banana', color='ffffff')

webhook.add_embed(embed)

response = webhook.execute()