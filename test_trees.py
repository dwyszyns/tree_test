import unittest
import matplotlib.pyplot as plt
from time import time
import mplcursors
from trees import AVL, BST


class TreesTests(unittest.TestCase):
    def test_bst_insert(self):
        bst = BST()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(17)
        self.assertEqual(bst.root.key, 10)
        self.assertEqual(bst.root.left.key, 5)
        self.assertEqual(bst.root.right.key, 15)
        self.assertEqual(bst.root.left.left.key, 3)
        self.assertEqual(bst.root.left.right.key, 7)
        self.assertEqual(bst.root.right.left.key, 12)
        self.assertEqual(bst.root.right.right.key, 17)

    def test_bst_delete(self):
        bst = BST()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(17)
        bst.insert(9)
        bst.insert(18)
        bst.delete(5)
        bst.delete(15)
        self.assertEqual(bst.root.key, 10)
        self.assertEqual(bst.root.left.key, 7)
        self.assertEqual(bst.root.right.key, 17)
        self.assertEqual(bst.root.left.left.key, 3)
        self.assertEqual(bst.root.right.left.key, 12)

    def test_bst_visualize_tree(self):
        bst_tree = BST()
        bst_tree.insert(50)
        bst_tree.insert(5)
        bst_tree.insert(80)
        bst_tree.insert(2)
        bst_tree.insert(40)
        bst_tree.insert(6)
        bst_tree.insert(70)
        bst_tree.insert(51)
        bst_tree.insert(41)
        bst_tree.insert(61)
        bst_tree.insert(81)
        bst_tree.insert(19)
        bst_tree.insert(31)
        bst_tree.insert(71)
        bst_tree.insert(21)
        bst_tree.insert(20)
        bst_tree.insert(18)
        bst_tree.insert(17)
        bst_tree.insert(16)
        bst_tree.insert(11)
        bst_tree.insert(8)
        bst_tree.insert(4)
        bst_tree.display()
        bst_tree.visualize_tree("bst_tree.png")

    def test_avl_insert(self):
        avl = AVL()
        avl.insert(10)
        avl.insert(5)
        avl.insert(15)
        avl.insert(3)
        avl.insert(7)
        avl.insert(12)
        avl.insert(17)
        self.assertEqual(avl.root.key, 10)
        self.assertEqual(avl.root.left.key, 5)
        self.assertEqual(avl.root.right.key, 15)
        self.assertEqual(avl.root.left.left.key, 3)
        self.assertEqual(avl.root.left.right.key, 7)
        self.assertEqual(avl.root.right.left.key, 12)
        self.assertEqual(avl.root.right.right.key, 17)

    def test_avl_delete(self):
        avl = AVL()
        avl.insert(10)
        avl.insert(5)
        avl.insert(15)
        avl.insert(3)
        avl.insert(7)
        avl.insert(12)
        avl.insert(17)
        avl.insert(9)
        avl.insert(18)
        avl.delete(5)
        avl.delete(15)
        self.assertEqual(avl.root.key, 10)
        self.assertEqual(avl.root.left.key, 7)
        self.assertEqual(avl.root.right.key, 17)
        self.assertEqual(avl.root.left.left.key, 3)
        self.assertEqual(avl.root.right.left.key, 12)

    def test_avl_visualize_tree(self):
        avl_tree = AVL()
        avl_tree.insert(50)
        avl_tree.insert(5)
        avl_tree.insert(80)
        avl_tree.insert(2)
        avl_tree.insert(40)
        avl_tree.insert(6)
        avl_tree.insert(70)
        avl_tree.insert(51)
        avl_tree.insert(41)
        avl_tree.insert(61)
        avl_tree.insert(81)
        avl_tree.insert(19)
        avl_tree.insert(31)
        avl_tree.insert(71)
        avl_tree.insert(21)
        avl_tree.insert(20)
        avl_tree.insert(18)
        avl_tree.insert(17)
        avl_tree.insert(16)
        avl_tree.insert(11)
        avl_tree.insert(8)
        avl_tree.insert(4)
        avl_tree.visualize_tree("avl_tree.png")

    def test_search(self):
        bst = BST()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(17)
        self.assertEqual(bst._search(bst.root, 10), bst.root)
        self.assertEqual(bst._search(bst.root, 5), bst.root.left)
        self.assertEqual(bst._search(bst.root, 15), bst.root.right)
        self.assertEqual(bst._search(bst.root, 3), bst.root.left.left)
        self.assertEqual(bst._search(bst.root, 7), bst.root.left.right)
        self.assertEqual(bst._search(bst.root, 12), bst.root.right.left)
        self.assertEqual(bst._search(bst.root, 17), bst.root.right.right)
        self.assertIsNone(bst._search(bst.root, 20))

    def test_delete_time(self):
        with open("random_numbers.txt", "r") as f:
            numbers = [int(line.strip()) for line in f]
            input_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 50000]
            trees_types = [BST(), AVL()]
            times = [[] for _ in range(len(trees_types))]
            for size in input_sizes:
                input_list = numbers[1:size]
                for i, tree in enumerate(trees_types):
                    for x in input_list:
                        tree.insert(x)
                    time_start = time()
                    for x in tree.get_all_numbers(tree.root):
                        tree.delete(x)
                    time_end = time()
                    times[i].append(time_end-time_start)
        plt.plot(input_sizes, times[0], label="BST")
        plt.plot(input_sizes, times[1], label="AVL")
        mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f'{sel.artist.get_label()}: {sel.target[1]:.6f} s'))
        plt.xlabel("Input size")
        plt.ylabel("Time (s)")
        plt.title("Trees deletion time")
        plt.legend()
        plt.savefig("tree_plot_deletion_time.png")
        plt.show()

    def test_add_time(self):
        with open("random_numbers.txt", "r") as f:
            numbers = [int(line.strip()) for line in f]
            input_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 50000]
            trees_types = [BST(), AVL()]
            times = [[] for _ in range(len(trees_types))]
            for size in input_sizes:
                input_list = numbers[1:size]
                for i, tree in enumerate(trees_types):
                    time_start = time()
                    for x in input_list:
                        tree.insert(x)
                    time_end = time()
                    times[i].append(time_end-time_start)
        plt.plot(input_sizes, times[0], label="BST")
        plt.plot(input_sizes, times[1], label="AVL")
        mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f'{sel.artist.get_label()}: {sel.target[1]:.6f} s'))
        plt.xlabel("Input size")
        plt.ylabel("Time (s)")
        plt.title("Trees add time")
        plt.legend()
        plt.savefig("tree_plot_add_time.png")
        plt.show()

    def test_search_time(self):
        with open("random_numbers.txt", "r") as f:
            numbers = [int(line.strip()) for line in f]
            input_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 50000]
            trees_types = [BST(), AVL()]
            times = [[] for _ in range(len(trees_types))]
            for size in input_sizes:
                input_list = numbers[1:size]
                for i, tree in enumerate(trees_types):
                    for x in input_list:
                        tree.insert(x)
                    time_start = time()
                    for x in tree.get_all_numbers(tree.root):
                        tree.search(x)
                    time_end = time()
                    times[i].append(time_end-time_start)
        plt.plot(input_sizes, times[0], label="BST")
        plt.plot(input_sizes, times[1], label="AVL")
        mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f'{sel.artist.get_label()}: {sel.target[1]:.6f} s'))
        plt.xlabel("Input size")
        plt.ylabel("Time (s)")
        plt.title("Trees search time")
        plt.legend()
        plt.savefig("tree_plot_search_time.png")
        plt.show()

    def test_get_all_numbers(self):
        bst = BST()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(17)
        self.assertEqual(bst.get_all_numbers(bst.root), [3, 5, 7, 10, 12, 15, 17])

        avl = AVL()
        avl.insert(10)
        avl.insert(5)
        avl.insert(15)
        avl.insert(3)
        avl.insert(7)
        avl.insert(12)
        avl.insert(17)
        self.assertEqual(avl.get_all_numbers(avl.root), [3, 5, 7, 10, 12, 15, 17])


if __name__ == "__main__":
    unittest.main()
