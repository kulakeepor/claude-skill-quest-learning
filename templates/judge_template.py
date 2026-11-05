# ============================================================
#  🎮 关卡 {LEVEL}：{TITLE}
#  目标：{GOAL}
#  规则：只修改 TODO 的地方，然后运行：python3 {FILENAME}
#  全部 ✅ 就通关！卡住了就说"{LEVEL} 任务X 要提示"
# ============================================================


# 任务 1：{描述 + 一个输入→输出例子}
def task1(x):
    # TODO
    return None


# 任务 2：{描述}
#   ⚠️ 规则：必须用到 for
def task2(x):
    # TODO
    return None


# ============================================================
#  ⬇️ 以下是裁判程序，不要修改 ⬇️
# ============================================================
def _judge():
    import inspect

    def body(fn):
        # 只检查学员写的部分（TODO 之后），避免注释里的字误触规则
        return inspect.getsource(fn).split("# TODO")[-1]

    # 规则/禁止道具：返回 True 表示合规，否则返回给学员看的说明
    rules = {
        task2: lambda s: "for " in s or "规则要求用到 for",
        # task3: lambda s: ("split" not in s and "import" not in s) or "禁止使用 split 或 import",
    }
    # (显示名, 函数, [(参数元组, 期望值), ...])  —— 一定要包含边界情况：空输入、单个元素、长度不足等
    tests = [
        ("任务1 名字", task1, [((1,), 2), ((0,), 1)]),
        ("任务2 名字", task2, [(([1, 2],), 3), (([],), 0)]),
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
        print("🏆 关卡 {LEVEL} 通关！告诉老师「{LEVEL} 通关」解锁下一关")
    else:
        print(f"进度 {passed}/{len(tests)}，继续加油！")


_judge()
