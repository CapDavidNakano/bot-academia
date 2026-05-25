import discord
from discord.ext import commands
import asyncio
import os  # OBLIGATORIO: Para leer los tokens en secreto sin que Discord los vea

# =============================================================
# ⚙️ CONFIGURACIÓN DE PERMISOS GENERALES
# =============================================================
intents = discord.Intents.default()
intents.members = True          # Recuerda activarlo en el Discord Developer Portal
intents.message_content = True  # Recuerda activarlo en el Discord Developer Portal

# =============================================================
# 🤖 BOT 1: MEISHO DOTO (CONTROL DE PRESENTACIONES E INGRESOS)
# =============================================================
bot_presentaciones = commands.Bot(command_prefix="?", intents=intents)

# 🆔 REEMPLAZA ESTAS IDS POR LAS DE TU SERVIDOR DE DISCORD
ID_CANAL_PRESENTACIONES = 1437195348949991618 
ID_ROL_TEMPORAL = 1508598332698792117         
ID_ROL_OFICIAL = 1508598587855212594          

@bot_presentaciones.event
async def on_ready():
    print(f"✓ Meisho Doto en línea como: {bot_presentaciones.user.name}")

@bot_presentaciones.event
async def on_member_join(member):
    rol_temporal = member.guild.get_role(ID_ROL_TEMPORAL)
    if rol_temporal:
        await member.add_roles(rol_temporal)

@bot_presentaciones.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == ID_CANAL_PRESENTACIONES:
        miembro = message.author
        rol_temporal = member.guild.get_role(ID_ROL_TEMPORAL)
        rol_oficial = member.guild.get_role(ID_ROL_OFICIAL)

        try:
            if rol_oficial and rol_oficial not in miembro.roles:
                await miembro.add_roles(rol_oficial)
            if rol_temporal and rol_temporal in miembro.roles:
                await miembro.remove_roles(rol_temporal)

            confirmacion = (
                f"✨🏆 ꧁𓊈𒆜★彡[ **ɪɴꜱᴄʀɪᴘᴄɪÓɴ ᴀᴘʀᴏʙᴀᴅᴀ** ]彡★𒆜𓊉꧂ 🐎✨\n\n"
                f"¡Felicidades, {miembro.mention}! Tu ficha ha sido registrada con éxito.\n"
                f"Se te ha otorgado el rango oficial de **{rol_oficial.name}**.\n\n"
                f"🏁 ¡La pista completa ha sido desbloqueada! Disfruta de la academia."
            )
            await message.channel.send(confirmacion, delete_after=15)
        except discord.Forbidden:
            print("❌ Error de permisos: Sube el rol del bot en los ajustes de Discord.")

    await bot_presentaciones.process_commands(message)

# =============================================================
# 📜 BOT 2: DAIWA SCARLET (CUSTODIO DEL MEGA-REGLAMENTO)
# =============================================================
bot_reglas = commands.Bot(command_prefix="!", intents=intents)

@bot_reglas.event
async def on_ready():
    print(f"✓ Daiwa Scarlet en línea como: {bot_reglas.user.name}")
    print("-----------------------------------------")
    print(" 🏁 ¡AMBOS MOTORES CORRIENDO EN PARALELO! ")
    print("-----------------------------------------")

@bot_reglas.command()
@commands.has_permissions(administrator=True)
async def desplegar_reglamento(ctx):
    """Envía las 32 reglas en bloques secuenciales"""
    await ctx.message.delete()

    bloque_1 = (
        "🏁🏆 ꧁𓊈𒆜★彡[ **ᴄÓᴅɪɢᴏ ᴏꜰɪᴄɪᴀʟ: ᴀᴄᴀᴅᴇᴍɪᴀ ᴛʀᴀᴄᴇɴ** ]彡★𒆜𓊉꧂ 🐎✨\n"
        "Bienvenidos a la normativa central de **The Uma-Prime Trophy**. El cumplimiento de estas normas garantiza tu permanencia en la pista.\n\n"
        "✨ **ᴄᴏɴᴠɪᴠᴇɴᴄɪᴀ ʏ ʀᴇꜱᴘᴇᴛᴏ ɢᴇɴᴇʀᴀʟ**\n"
        "•| 01 **[ʀᴇꜱᴘᴇᴛᴏ ᴍᴜᴛᴜᴏ]** – Se prohíben insultos, menosprecios o actitudes agresivas hacia cualquier miembro.\n"
        "•| 02 **[ᴀɴᴛɪ-ᴛᴏxɪᴄɪᴅᴀᴅ]** – No se tolerará drama innecesario, quejas constantes o actitudes que arruinen la vibra del servidor.\n"
        "•| 03 **[ᴅɪꜱᴄʀɪᴍɪɴᴀᴄɪÓɴ ᴄᴇʀᴏ]** – Prohibido cualquier comentario discriminatorio por raza, nacionalidad, género u orientación.\n"
        "•| 04 **[ʟᴇɴɢᴜᴀᴊᴇ ᴀᴅᴇᴄᴜᴀᴅᴏ]** – Modera el uso de groserías vulgares. Mantengamos un ambiente sofisticado.\n"
        "•| 05 **[ᴀᴄᴏꜱᴏ ʏ ʜᴏꜱᴛɪɢᴀᴍɪᴇɴᴛᴏ]** – Perseguir, molestar o mandar mensajes directos no deseados a miembros resultará en ban inmediato.\n"
        "•| 06 **[ɪᴅᴇɴᴛɪᴅᴀᴅ ᴇɴ ʟᴀ ᴘɪꜱᴛᴀ]** – No utilices nombres de usuario o fotos de perfil que resulten ofensivas, obscenas o difamatorias.\n"
        "•| 07 **[ᴍᴇɴᴄɪᴏɴᴇꜱ ɪɴɴᴇᴄᴇꜱᴀʀɪᴀꜱ]** – Queda prohibido spamear menciones (`@everyone`, `@here`) o etiquetar al Staff sin un motivo real.\n"
        "•| 08 **[ꜱᴏᴘᴏʀᴛᴇ ʏ ᴄᴀɴᴀʟᴇꜱ]** – Los problemas personales o reportes de fallos se manejan por privado o en soporte, no en canales públicos."
    )

    bloque_2 = (
        "✨ **ʀᴇɢɪꜱᴛʀᴏ, ᴘʀɪᴠᴀᴄɪᴅᴀᴅ ʏ ꜱᴇɢᴜʀɪᴅᴀᴅ**\n"
        "•| 09 **[ꜰɪᴄʜᴀ ᴏʙʟɪɢᴀᴛᴏʀɪᴀ]** – Es un requisito indispensable rellenar la ficha en presentaciones para validar tu cuenta.\n"
        "•| 10 **[ᴘʟᴀᴢᴏ ᴅᴇ ɪɴꜱᴄʀɪᴘᴄɪÓɴ]** – Cuentas con un máximo de 24 horas para presentarte antes de ser retirado por sospecha de bot.\n"
        "•| 11 **[ᴠᴇʀɪꜰɪᴄᴀᴄɪÓɴ ʀᴇᴀʟ]** – No uses respuestas genéricas de una palabra en tu ficha. Queremos entrenadores reales.\n"
        "•| 12 **[ᴘʀɪᴠᴀᴄɪᴅᴀᴅ ᴅᴇ ᴅᴀᴛᴏꜱ]** – No compartas datos privados sensibles como direcciones exactas o números telefónicos.\n"
        "•| 13 **[ᴄᴇʀᴏ ᴇɴʟᴀᴄᴇꜱ ᴇxᴛᴇʀɴᴏꜱ]** – Queda estrictamente prohibido colocar links de invitación a otros servidores o grupos en tu ficha.\n"
        "•| 14 **[ᴀɴᴛɪ-ᴇꜱᴘɪᴏɴᴀᴊᴇ]** – Usuarios que entren solo para sustraer miembros hacia otras redes serán baneados permanentemente.\n"
        "•| 15 **[ꜱᴇɢᴜʀɪᴅᴀᴅ ᴅɪɢɪᴛᴀʟ]** – Prohibido distribuir archivos ejecutables dañinos, software malicioso o herramientas de hackeo.\n"
        "•| 16 **[ᴄᴜᴇɴᴛᴀꜱ ᴀʟᴛᴇʀɴᴀꜱ]** – No se permite el uso de multicuentas (alts) para evadir sanciones o alterar las mecánicas del servidor."
    )

    bloque_3 = (
        "✨ **ᴍᴜʟᴛɪᴍᴇᴅɪᴀ, ᴀɴɪᴍᴇ, ᴍÚꜱɪᴄᴀ ʏ ʙᴏᴛꜱ**\n"
        "•| 17 **[ᴢᴏɴᴀ ʟɪᴍᴘɪᴀ ꜱꜰᴡ]** – Prohibido terminantemente compartir imágenes, videos o textos de carácter explícito, erótico o NSFW (+18).\n"
        "•| 18 **[ᴀʟᴇʀᴛᴀ ᴅᴇ ꜱᴘᴏɪʟᴇʀꜱ]** – Usa las barras de censura (`||texto||`) al hablar de mangas recientes o capítulos de estreno.\n"
        "•| 19 **[ᴏʀᴅᴇɴ ᴍᴜʟᴛɪᴍᴇᴅɪᴀ]** – No satures los canales con ráfagas de 20 imágenes o videos seguidos. Comparte con moderación.\n"
        "•| 20 **[ᴄᴏᴍᴀɴᴅᴏꜱ ᴇɴ ꜱᴜ ʟᴜɢᴀʀ]** – Los comandos de bots (Nekotina/Unbelieva) se usan única y exclusivamente en sus respectivas salas.\n"
        "•| 21 **[ᴀɴᴛɪ-ꜱᴘᴀᴍ ᴅᴇ ʙᴏᴛꜱ]** – No envíes cadenas masivas de comandos. Dale tiempo al bot para procesar la petición anterior.\n"
        "•| 22 **[ᴊᴜᴇɢᴏ ʟɪᴍᴘɪᴏ ʏ ᴀᴘᴜᴇꜱᴛᴀꜱ]** – Las deudas o pérdidas virtuales dentro del casino de los bots son entera responsabilidad del jugador.\n"
        "•| 23 **[ᴄʀÉᴅɪᴛᴏꜱ ᴅᴇ ᴀʀᴛᴇ]** – Al compartir fanarts, diseños automotrices o dibujos ajenos, intenta dar el debido crédito al autor.\n"
        "•| 24 **[ʀᴇꜱᴘᴇᴛᴏ ᴇꜱᴛÉᴛɪᴄᴏ]** – No uses los canales de arte o autos para subir imágenes borrosas, distorsionadas o de pésima calidad."
    )

    bloque_4 = (
        "✨ **ɢᴀᴍɪɴɢ, ᴠᴏᴢ ʏ ᴘᴇʀᴍᴀɴᴇɴᴄɪᴀ ᴇɴ ʟᴀ ᴀᴄᴀᴅᴇᴍɪᴀ**\n"
        "•| 25 **[ꜱᴇʀᴠɪᴅᴏʀ ᴍɪɴᴇᴄʀᴀꜰᴛ]** – Prohibido el griefing, robo o destrucción en las zonas residenciales o técnicas de los demás.\n"
        "•| 26 **[ᴊᴜᴇɢᴏ ʟɪᴍᴘɪᴏ]** – El uso de X-Ray, hacks o modificaciones que den ventajas injustas en Minecraft está penalizado con ban.\n"
        "•| 27 **[ᴘᴠᴘ ᴘᴀᴄÍꜰɪᴄᴏ]** – No se permite atacar a otros jugadores a menos que ambos acuerden un duelo de forma amistosa.\n"
        "•| 28 **[ᴄᴀɴᴀʟᴇꜱ ᴅᴇ ᴠᴏᴢ]** – Queda prohibido gritar, soplar el micrófono o reproducir sonidos estridentes en las salas de voz.\n"
        "•| 29 **[ᴍÚꜱɪᴄᴀ ᴇɴ ʟʟᴀᴍᴀᴅᴀꜱ]** – Si estás usando un bot de música en canal de voz, respeta los turnos de la lista de reproducción.\n"
        "•| 30 **[ʟɪᴍᴘɪᴇᴢᴀ ᴅᴇ ᴄᴜᴘᴏꜱ]** – La inactividad extrema y prolongada sin previa justificación causará la baja para mantener libre la pista.\n"
        "•| 31 **[ꜰᴇꜱᴛᴇᴊᴏꜱ ᴅᴇ ᴄᴜᴍᴘʟᴇᴀÑᴏꜱ]** – No utilices los canales festivos para exigir regalos, roles de pago o transacciones reales.\n"
        "•| 32 **[ᴀᴜᴛᴏʀɪᴅᴀᴅ ᴅᴇʟ ᴄᴏᴍɪᴛé]** – Las decisiones de los administradores en cuanto a sanciones y orden son finales y se deben acatar.\n\n"
        "🏁 **¡Cruza la línea de meta!** El desconocimiento de este reglamento no exime de su cumplimiento. Disfruta de la experiencia definitiva en **The Uma-Prime Trophy**."
    )

    await ctx.send(bloque_1)
    await asyncio.sleep(1)
    await ctx.send(bloque_2)
    await asyncio.sleep(1)
    await ctx.send(bloque_3)
    await asyncio.sleep(1)
    await ctx.send(bloque_4)

@bot_reglas.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ No tienes la autoridad del Comité Tracen para usar este comando.", delete_after=5)

# =============================================================
# 🚀 ARRANQUE SEGURO CON VARIABLES DE ENTORNO
# =============================================================
async def main():
    # El sistema jala los tokens guardados en Render de forma invisible
    TOKEN_BOT_PRESENTACIONES = os.environ.get("MTQ2MzMwNDgwMjQxMzk2OTQ4OQ.GLsXyC.DdcTQdPwmEQJJo0aUB79e-TFP8xVt7g_bLf1Lw")
    TOKEN_BOT_REGLAS = os.environ.get("MTI4Mjg5MDc4MDgwNDkxMTIwOA.GPyNVD.QEpYcSeS0CTHlHcENE3GpSw7jJHQ8is__08fk4")
    
    await asyncio.gather(
        bot_presentaciones.start(MTQ2MzMwNDgwMjQxMzk2OTQ4OQ.GLsXyC.DdcTQdPwmEQJJo0aUB79e-TFP8xVt7g_bLf1Lw),
        bot_reglas.start(MTI4Mjg5MDc4MDgwNDkxMTIwOA.GPyNVD.QEpYcSeS0CTHlHcENE3GpSw7jJHQ8is__08fk4)
    )

if __name__ == "__main__":
    asyncio.run(main())
