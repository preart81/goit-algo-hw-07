from tree.avl_tree import insert, max_value_node, min_value_node, sum_of_nodes

root = None

keys = [10, 20, 30, 25, 28, 27, -1]

print(f"Створюємо AVL-дерево:")
for key in keys:
    root = insert(root, key)
    # Процес заповнення дерева
    # print(f"Вставлено: {key}")
    # print("AVL-Дерево:")
    # print(root)

print("AVL-Дерево:")
print(root)


print(f"Максимальный елемент: {max_value_node(root).__str__(prefix='Node ')}")
print(f"Мінімальный елемент: {min_value_node(root).__str__(prefix='Node ')}")
print(f"Сума всіх елементів: {sum_of_nodes(root)}")
