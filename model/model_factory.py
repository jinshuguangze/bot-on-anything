"""
channel factory
"""

from common import const

def create_bot(model_type):
    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """

    if model_type == const.GPT_3:
        # OpenAI 官方对话模型API (gpt-3.0)
        from model.openai.gpt_3_model import Gpt_3_Model
        return Gpt_3_Model()

    elif model_type == const.GPT_3_5:
        # ChatGPT API (gpt-3.5-turbo)
        from model.openai.gpt_3_5_model import Gpt_3_5_Model
        return Gpt_3_5_Model()
    
    elif model_type == const.GPT_4:
        # ChatGPT API (gpt-4)
        from model.openai.gpt_4_model import Gpt_4_Model
        return Gpt_4_Model()
    
    elif model_type == const.BAIDU:
        from model.baidu.yiyan_model import YiyanModel
        return YiyanModel()

    elif model_type == const.BING:
        from model.microsoft.new_bing_model import BingModel
        return BingModel()

    elif model_type == const.BARD:
        from model.google.bard_model import BardModel
        return BardModel()

    raise RuntimeError
