def ft_tqdm(lst: range) -> None:
    """
    Basic tqdm function.
    """
    print("100%|[", end="")
    progress = len(lst)
    remaining = 100
    current = 0
    for elem in lst:
        progress -= 1
        current += 1
        if (current > len(lst) / 100):
            current = 0
            remaining -= 1
            print("=", end="")
        yield elem
    print(f">]| {len(lst)}/{len(lst)}")