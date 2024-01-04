def ft_filter(function_to_apply, list_of_inputs):
    """
        filter(function or None, iterable) --> filter object

        Return an iterator yielding those items of iterable
        for which function(item) is true.
        If function is None, return the items that are true.
    """
    if function_to_apply is None:
        return [x for x in list_of_inputs if x]
    return [x for x in list_of_inputs if function_to_apply(x)]

if __name__ == "__main__":
    main()
