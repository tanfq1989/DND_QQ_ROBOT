from aiocqhttp import CQHttp
import dice
import attribute_controller
import user_gen
import helper
import base_filter

bot = CQHttp(access_token='yowasaTest',
             enable_http_post=False)


@bot.on_message()
async def handle_msg(context):
    content = context.copy()

    result = base_filter.filter(content)
    if result:
        return await bot.send(context, result)
    print(context)
    commond = context['message']
    result = None
    # 骰点
    if commond.startswith('.r') and not commond.startswith('.race') and not commond.startswith('.reroll'):
        result = dice.dice_ex(context)
    # 统一发送消息
    if result != None:
        await bot.send(context, result)


# @bot.on_notice('group_increase')
# async def handle_group_increase(context):
#     await bot.send(context, message='欢迎新人～',
#                    at_sender=True, auto_escape=True)
#
#
# @bot.on_request('group', 'friend')
# async def handle_request(context):
#     return {'approve': True}

# 初始化过滤器
base_filter.init('dnd/plugins')

bot.run(host='127.0.0.1', port=8080)
