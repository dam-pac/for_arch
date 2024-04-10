# -*- coding: utf-8 -*-
#Загрузка библиотек
import disnake
from disnake import Option
from disnake.ext import commands
from disnake.embeds import Embed
from keep_alive import keep_alive
#!МЕСТО ДЛЯ ТОКЕНА БОТА!
token = "MTE5MzY1MDIwMTI3NDA4OTUzMg.G2pU-3.pzI97tvm6ukW8_MsVh0V9ESCDJOWpQjtiMLWuM"

emoji_perl = "<:perl:1167865266479321209>"
version = "0.2.1.DATA_BASE"
# Начало кода бота
#Инициализация бота
intents = disnake.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)


#Вывод сообщения об успешном входе
@bot.event
async def on_ready():
  print(f'Бот вошёл в дискорд под именем {bot.user.name}.')


@bot.command(pass_context=True)
async def custom_role(ctx, role_name: str, user: disnake.Member,
                      hex_color: str):
  user_id = ctx.author.id
  if user_id == 761668841642000384:
    guild = bot.get_guild(1095590756208619552)
    role = await guild.create_role(name=f"{role_name}",
                                   color=disnake.Color(int(hex_color, 16)))
    member = guild.get_member(user.id)
    await member.add_roles(role)
    await ctx.reply(
        f"Ваша кастомная роль {role.mention} успешно создана и выдана Вам!")
  else:
    await ctx.reply(f'Чужой запрос')


#Запуск бота

keep_alive()
bot.run(token)