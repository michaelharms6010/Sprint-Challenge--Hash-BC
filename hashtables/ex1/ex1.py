from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        if hash_table_retrieve(ht, limit - weights[i]) is not None:
            return(i, hash_table_retrieve(ht, limit - weights[i]))
        else:
            hash_table_insert(ht, weights[i], i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
