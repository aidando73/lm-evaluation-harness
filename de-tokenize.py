
# import transformers
# import torch

model_id = "meta-llama/Llama-3.2-1B"

# pipeline = transformers.pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto")
# out = pipeline("Hey how are you doing today?")

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(model_id)

tokens=[
            128000,
            791,
            2768,
            527,
            5361,
            5873,
            4860,
            320,
            4291,
            11503,
            8,
            922,
            36256,
            38696,
            382,
            791,
            7187,
            315,
            279,
            3363,
            1405,
            33126,
            574,
            9405,
            374,
            220,
            9591,
            11,
            23038,
            13,
            3639,
            374,
            279,
            907,
            315,
            279,
            220,
            20,
            304,
            279,
            1396,
            220,
            9591,
            11,
            23038,
            5380,
            32,
            13,
            220,
            20,
            9214,
            198,
            33,
            13,
            220,
            20,
            11758,
            198,
            34,
            13,
            220,
            20,
            22781,
            198,
            35,
            13,
            220,
            20,
            6305,
            198,
            16533,
            25,
            362,
            271,
            43819,
            21475,
            1511,
            279,
            6037,
            330,
            2261,
            220,
            806,
            1,
            311,
            1893,
            279,
            1396,
            5497,
            6982,
            3770,
            13,
            220,
            605,
            11,
            220,
            1691,
            11,
            220,
            843,
            11,
            220,
            3391,
            11,
            220,
            4370,
            16299,
            5224,
            922,
            279,
            1396,
            5497,
            374,
            837,
            5380,
            32,
            13,
            578,
            220,
            605,
            339,
            1396,
            304,
            279,
            5497,
            690,
            387,
            459,
            1524,
            1396,
            627,
            33,
            13,
            578,
            1396,
            5497,
            690,
            2646,
            617,
            1403,
            1524,
            5219,
            1828,
            311,
            1855,
            1023,
            627,
            34,
            13,
            578,
            1828,
            1403,
            5219,
            304,
            279,
            5497,
            690,
            387,
            459,
            1524,
            1396,
            1243,
            459,
            10535,
            1396,
            627,
            35,
            13,
            1442,
            279,
            1396,
            5497,
            3940,
            449,
            459,
            10535,
            1396,
            1243,
            279,
            5497,
            1053,
            617,
            1193,
            10535,
            5219,
            304,
            433,
            627,
            16533,
            25,
            426,
            271,
            32,
            2860,
            315,
            220,
            966,
            4311,
            690,
            1514,
            19794,
            520,
            264,
            6246,
            13,
            2684,
            690,
            387,
            7041,
            220,
            20,
            4311,
            389,
            1855,
            2128,
            13,
            16299,
            5224,
            12722,
            15100,
            1268,
            311,
            1505,
            279,
            1396,
            315,
            7411,
            4460,
            5380,
            32,
            13,
            2758,
            220,
            20,
            311,
            220,
            966,
            311,
            1505,
            220,
            1758,
            7411,
            627,
            33,
            13,
            64002,
            220,
            966,
            555,
            220,
            20,
            311,
            1505,
            220,
            21,
            7411,
            627,
            34,
            13,
            72159,
            220,
            966,
            323,
            220,
            20,
            311,
            1505,
            220,
            3965,
            7411,
            627,
            35,
            13,
            94310,
            220,
            20,
            505,
            220,
            966,
            311,
            1505,
            220,
            914,
            7411,
            627,
            16533,
            25,
            426,
            271,
            32,
            3637,
            31878,
            220,
            7699,
            2204,
            8146,
            315,
            6308,
            13,
            2435,
            617,
            220,
            914,
            43732,
            315,
            1855,
            1933,
            304,
            5942,
            13,
            578,
            1396,
            315,
            43732,
            315,
            6308,
            279,
            3637,
            706,
            304,
            5942,
            649,
            387,
            1766,
            1701,
            279,
            7645,
            3770,
            13,
            220,
            7699,
            25800,
            220,
            914,
            13,
            2650,
            1690,
            43732,
            315,
            6308,
            1587,
            279,
            3637,
            617,
            304,
            5942,
            5380,
            32,
            13,
            220,
            25541,
            198,
            33,
            13,
            220,
            17,
            11,
            21129,
            198,
            34,
            13,
            220,
            17,
            11,
            24599,
            198,
            35,
            13,
            220,
            19,
            11,
            5154,
            198,
            16533,
            25,
            426,
            271,
            23956,
            7645,
            374,
            13890,
            311,
            220,
            20,
            865,
            220,
            24,
            5380,
            32,
            13,
            320,
            20,
            865,
            220,
            19,
            8,
            865,
            320,
            21,
            865,
            220,
            20,
            340,
            33,
            13,
            320,
            20,
            865,
            220,
            20,
            8,
            489,
            320,
            20,
            865,
            220,
            19,
            340,
            34,
            13,
            320,
            20,
            865,
            220,
            20,
            8,
            489,
            320,
            20,
            865,
            220,
            24,
            340,
            35,
            13,
            320,
            20,
            865,
            220,
            24,
            8,
            865,
            320,
            21,
            865,
            220,
            24,
            340,
            16533,
            25,
            426,
            271,
            11874,
            4459,
            5219,
            617,
            264,
            3325,
            4279,
            5361,
            315,
            220,
            1399,
            13,
            9062,
            1396,
            374,
            2753,
            1109,
            477,
            6273,
            311,
            220,
            717,
            13,
            578,
            12474,
            4279,
            8331,
            315,
            279,
            1403,
            5219,
            285,
            220,
            17,
            13,
            3639,
            527,
            279,
            1403,
            5219,
            5380,
            32,
            13,
            220,
            21,
            323,
            220,
            605,
            198,
            33,
            13,
            220,
            20,
            323,
            220,
            717,
            198,
            34,
            13,
            220,
            605,
            323,
            220,
            717,
            198,
            35,
            13,
            220,
            717,
            323,
            220,
            868,
            198,
            16533,
            25,
            356,
        ]

tokens = [128000]

print(tokenizer.decode(tokens))

# print(tokenizer.encode("A"))
# print(tokenizer.encode("B"))
# print(tokenizer.encode("C"))
# print(tokenizer.encode("D"))
print(tokenizer.encode(" "))