import json
import unittest

import os
import sys
sys.path.insert(1, os.getcwd())  # Ensure the current directory is in the path

from rdagent.oai.llm_utils import APIBackend
from rdagent.utils.env import QlibCondaConf, QlibCondaEnv


class TestChatCompletion(unittest.TestCase):
    # def test_chat_completion(self) -> None:
    #     system_prompt = "You are a helpful assistant."
    #     user_prompt = "What is your name?"
    #     response = APIBackend().build_messages_and_create_chat_completion(
    #         system_prompt=system_prompt,
    #         user_prompt=user_prompt,
    #     )
    #     assert response is not None
    #     assert isinstance(response, str)

    # def test_chat_completion_json_mode(self) -> None:
    #     system_prompt = "You are a helpful assistant. answer in Json format."
    #     user_prompt = "What is your name?"
    #     response = APIBackend().build_messages_and_create_chat_completion(
    #         system_prompt=system_prompt,
    #         user_prompt=user_prompt,
    #         json_mode=True,
    #     )
    #     assert response is not None
    #     assert isinstance(response, str)
    #     json.loads(response)

    # def test_build_messages_and_calculate_token(self) -> None:
    #     system_prompt = "You are a helpful assistant."
    #     user_prompt = "What is your name?"
    #     token = APIBackend().build_messages_and_calculate_token(user_prompt=user_prompt, system_prompt=system_prompt)
    #     assert token is not None
    #     assert isinstance(token, int)

    def test_chat_completion_json_mode(self) -> None:
        qtde = QlibCondaEnv(conf=QlibCondaConf())
        execute_qlib_log = qtde.run(
            local_path="E:\\RD-Agent\\git_ignore_folder\\RD-Agent_workspace\\808434d04feb451d90565828505a54e9",
            entry="qrun conf.yaml",
            env={"PATH": ":/bin/:/usr/bin/:"},
        )

    # def test_embedding(self) -> None:
    #     res = APIBackend().create_embedding(
    #         input_content='factor_name: 10_day_momentum\nfactor_description: [Momentum Factor] The 10-day momentum factor calculates the percentage change in the adjusted close price over the past 10 trading days.\nfactor_formulation: M_{10} = \\frac{close_t - close_{t-10}}{close_{t-10}}\nvariables: {\'close_t\': "current day\'s adjusted close price", \'close_{t-10}\': \'adjusted close price 10 trading days ago\'}'
    #     )
    #     print(res)
    
if __name__ == "__main__":
    unittest.main()
