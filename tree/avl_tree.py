class AVLNode:
    """
    AVL-дерево

    https://en.wikipedia.org/wiki/AVL_tree
    """

    def __init__(self, key):
        """
        Конструктор

        Параметри:
            key: ключ
        """
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: ") -> str:
        """
        Візуалізація дерева

        Параметри:
            level: початковий рівень дерева
            prefix: префікс, дефолт = 'Root: '

        Повертає:
            ret: багаторядкова текстова візуалізація дерева
        """

        ret = "\t" * level + prefix + str(self.key) + "\n"

        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")

        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")

        return ret


def get_height(node: AVLNode) -> int:
    """
    Повертає висоту дерева

    Параметри:
        node: вузол дерева
    """
    if not node:
        return 0
    return node.height


def get_balance(node: AVLNode) -> int:
    """
    Повертає баланс вказаного вузла як різницю висот left - right

    Параметри:
        node: вузол дерева

    Повертає:
        balance: баланс вказаного вузла
    """
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def left_rotate(z: AVLNode):
    """
    Обертання ліворуч

    Параметри:
        z : вузол для обертання
    """
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def right_rotate(y: AVLNode):
    """
    Обертання праворуч

    Параметри:
        y : вузол для обертання
    """
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def insert(root: AVLNode, key):
    """
    Вставка в AVL-дерево

    Параметри:
        root: AVL-дерево
        key: ключ для вставки
    """
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def delete_node(root: AVLNode, key):
    """
    Видалення вузла з AVL-дерева

    Параметри:
        root: AVL-дерево
        key: ключ для видалення
    """
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    if root is None:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if get_balance(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if get_balance(root.right) <= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def min_value_node(node: AVLNode) -> AVLNode:
    """
    Повертає вузол з найменшим значенням серед дочірніх вузлів заданого вузла

    Параметри:
        node: вузол дерева
    """
    current = node
    while current.left is not None:
        current = current.left
    return current


def max_value_node(node: AVLNode) -> AVLNode:
    """
    Повертає вузол з найбільшим значенням серед дочірніх вузлів заданого вузла

    Параметри:
        node: вузол дерева
    """
    current = node
    while current.right is not None:
        current = current.right
    return current


def sum_of_nodes(node: AVLNode) -> int | float:
    """
    Повертає суму елементів дерева серед дочірніх вузлів заданого вузла

    Параметри:
        node: вузол дерева
    """
    if not node:
        return 0
    return node.key + sum_of_nodes(node.left) + sum_of_nodes(node.right)


if __name__ == "__main__":
    # Тестування
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]
    # keys = [-1, 10, 20, 25, 27, 28, 30]

    for key in keys:
        root = insert(root, key)
        print(f"Вставлено:", key, "-" * 40)
        print("AVL-Дерево:")
        print(root)

    print(f"{'Максимальний елемент:':-<50}")
    print(f"{max_value_node(root).__str__(prefix='Node: ')}")

    print(f"{'Мінімальний елемент:':-<50}")
    print(f"{min_value_node(root).__str__(prefix='Node: ')}")

    print(f"{'Сума всіх елементів:':-<50}")
    print(f"{sum_of_nodes(root)}")

    # Delete
    keys_to_delete = [10, 27]
    for key in keys_to_delete:
        root = delete_node(root, key)
        print("Видалено:", key, "-" * 40)
        print("AVL-Дерево:")
        print(root)

    print(f"{'Максимальний елемент:':-<50}")
    print(f"{max_value_node(root).__str__(prefix='Node: ')}")

    print(f"{'Мінімальний елемент:':-<50}")
    print(f"{min_value_node(root).__str__(prefix='Node: ')}")

    print(f"{'Сума всіх елементів:':-<50}")
    print(f"{sum_of_nodes(root)}")
