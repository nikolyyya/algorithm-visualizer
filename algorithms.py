# algorithms.py
def bubble_sort_steps(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    passes = 0
    steps = 0

    for i in range(n - 1):
        swapped = False
        passes += 1

        for j in range(n - 1 - i):
            comparisons += 1
            steps += 1
            yield {
                "type": "compare",
                "indices": (j, j + 1),
                "sorted_from": n - i,
                "stats": {"comparisons": comparisons, "swaps": swaps,
                          "pass": passes, "steps": steps},
            }

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                swaps += 1
                steps += 1
                yield {
                    "type": "swap",
                    "indices": (j, j + 1),
                    "sorted_from": n - i,
                    "stats": {"comparisons": comparisons, "swaps": swaps,
                              "pass": passes, "steps": steps},
                }

        steps += 1
        yield {
            "type": "pass_end",
            "indices": None,
            "sorted_from": n - i - 1,
            "stats": {"comparisons": comparisons, "swaps": swaps,
                      "pass": passes, "steps": steps},
        }

        if not swapped:     
            break

    steps += 1
    yield {
        "type": "done",
        "indices": None,
        "sorted_from": 0,
        "stats": {"comparisons": comparisons, "swaps": swaps,
                  "pass": passes, "steps": steps},
    }


def selection_sort_steps(arr):
    n = len(arr)
    comparisons = swaps = passes = steps = 0

    def make(step_type, indices, min_idx, sorted_upto):
        return {
            "type": step_type,
            "indices": indices,
            "min_idx": min_idx,
            "sorted_upto": sorted_upto,
            "stats": {"comparisons": comparisons, "swaps": swaps,
                      "pass": passes, "steps": steps, "min_index": min_idx},
        }

    for i in range(n - 1):
        min_idx = i
        passes += 1
        for j in range(i + 1, n):
            comparisons += 1
            steps += 1
            yield make("compare", (j, min_idx), min_idx, i)
            if arr[j] < arr[min_idx]:
                min_idx = j
                steps += 1
                yield make("new_min", (j,), min_idx, i)
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            steps += 1
            yield make("swap", (i, min_idx), min_idx, i)
        steps += 1
        yield make("pass_end", None, None, i + 1)

    steps += 1
    yield make("done", None, None, n)


def binary_search_steps(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = steps = 0

    def make(step_type, mid, result):
        return {
            "type": step_type,
            "left": left,
            "mid": mid,
            "right": right,
            "stats": {
                "target": target,
                "comparisons": comparisons,
                "steps": steps,
                "current_range": (left, right),
                "result": result,
            },
        }

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        steps += 1
        yield make("compare", mid, None)

        if arr[mid] == target:
            steps += 1
            yield make("found", mid, mid)
            return

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    steps += 1
    yield make("not_found", None, -1)

