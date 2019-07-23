def move_cheeses(n: int, source: int, intermediate: int,
                 destination: int) -> None:
    """Print moves to get n cheeses from source to destination, possibly
    using intermediate"""
    if n > 1:
        move_cheeses(n - 1, source, destination, intermediate)
        move_cheeses(1, source, intermediate, destination)
        move_cheeses(n -1, intermediate, source, destination)
    else: # just one cheese --- no recursion required!
        print("Move top cheese from {} to {}".format(source, destination))