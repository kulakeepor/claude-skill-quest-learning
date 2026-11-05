# ============================================================
#  🎮 关卡 0-3：火眼金睛
#  目标：学会"if 条件判断"，让程序自己做决定
#  规则：只修改 TODO 的地方，然后运行：python3 level_0-3.py
#  全部 ✅ 就通关！卡住了就跟 Claude 说"0-3 任务X 要提示"
# ============================================================

PUNCT = "，。！？、；："   # 这关用到的所有标点


# 任务 1：判断一个字是不是标点，是就返回 True，不是就返回 False
#   is_punct("，") → True      is_punct("月") → False
def is_punct(ch):
    # TODO
    return None


# 任务 2：去掉文字里所有的标点
#   "床前明月光，疑是地上霜。" → "床前明月光疑是地上霜"
#   ⚠️ 规则：必须用到 if
def remove_punct(text):
    # TODO
    return None


# 任务 3：找出出现了不止一次的字（不算标点）
#   按第一次出现的顺序排列，每个字只列一次
#   "举头望明月，低头思故乡" → ["头"]
#   "春眠不觉晓，处处闻啼鸟" → ["处"]
#   ⚠️ 规则：必须用到 if
def repeated_chars(text):
    # TODO
    return None


# 任务 4（挑战）：按标点把一首诗切成一句一句
#   "床前明月光，疑是地上霜。" → ["床前明月光", "疑是地上霜"]
#   连续的标点或开头结尾的标点不能产生空句子 ""
#   ⚠️ 禁止道具：不许用 split，也不许 import 任何东西，要自己一个字一个字地走
def split_sentences(text):
    # TODO
    return None


# ============================================================
#  ⬇️ 以下是裁判程序，不要修改 ⬇️
# ============================================================
def _judge():
    import inspect
    def body(fn):
        return inspect.getsource(fn).split("# TODO")[-1]
    rules = {
        remove_punct: lambda s: "if " in s or "规则要求用到 if",
        repeated_chars: lambda s: "if " in s or "规则要求用到 if",
        split_sentences: lambda s: ("split" not in s and "import" not in s) or "禁止使用 split 或 import",
    }
    tests = [
        ("任务1 认标点", is_punct, [(("，",), True), (("。",), True), (("月",), False), (("？",), True), (("a",), False)]),
        ("任务2 去标点", remove_punct, [(("床前明月光，疑是地上霜。",), "床前明月光疑是地上霜"), (("春眠",), "春眠"), (("，。！",), ""), (("",), "")]),
        ("任务3 找重复", repeated_chars, [(("举头望明月，低头思故乡",), ["头"]), (("春眠不觉晓，处处闻啼鸟",), ["处"]),
                                       (("明月明月光，，",), ["明", "月"]), (("床前明月光",), [])]),
        ("任务4 切句子", split_sentences, [(("床前明月光，疑是地上霜。",), ["床前明月光", "疑是地上霜"]),
                                        (("春眠不觉晓",), ["春眠不觉晓"]), (("，，白日依山尽。。黄河入海流！",), ["白日依山尽", "黄河入海流"]),
                                        (("。",), []), (("",), [])]),
    ]
    passed = 0
    for name, fn, cases in tests:
        if fn in rules:
            r = rules[fn](body(fn))
            if r is not True:
                print(f"❌ {name}：{r}")
                continue
        ok = True
        for args, want in cases:
            try:
                got = fn(*args)
            except Exception as e:
                print(f"❌ {name}：程序出错了 → {type(e).__name__}: {e}")
                ok = False
                break
            if got != want:
                shown = ", ".join(repr(a) for a in args)
                print(f"❌ {name}：输入 {shown}，期望 {want!r}，你返回了 {got!r}")
                ok = False
                break
        if ok:
            print(f"✅ {name}")
            passed += 1
    print("-" * 40)
    if passed == len(tests):
        print("🏆 关卡 0-3 通关！告诉 Claude「0-3 通关」解锁下一关")
    else:
        print(f"进度 {passed}/{len(tests)}，继续加油！")

_judge()
