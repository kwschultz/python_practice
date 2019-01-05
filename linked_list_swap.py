# Testing my solution to swapping the kth and N-kth elements in linked list.

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self, head):
        self.head = head

def print_list(list):
    node = list.head
    while(node):
        print(node.data)
        node = node.next

def swap_k_and_n_m_k(linked_list, k):

    assert k > 0
    this_node = linked_list.head
    node_counter = 1
    k_m_1_pointer, k_pointer, k_p_1_pointer = None, None, None
    n_m_k_m_1_pointer, n_m_k_pointer, n_m_k_p_1_pointer = None, None, None

    # Notation: N_m_k = “N minus k”, k_p_1 = “k plus one”, etc.

    while(this_node is not None):
        if node_counter == k-1:
            k_m_1_pointer = this_node
            print("k-1: {}".format(k_m_1_pointer))
        elif node_counter == k:
            k_pointer = this_node
            print("k: {}".format(k_pointer))
        elif node_counter == k+1:
            k_p_1_pointer = this_node
            print("k+1: {}".format(k_p_1_pointer))
        
        # take the next step in the list
        this_node = this_node.next
        node_counter += 1

    # We've stepped through once, so now we know N.
    N = node_counter - 1
    print("N = {}".format(N))
    # reset the counter for the next iteration
    node_counter = 1
    this_node = linked_list.head

    while(this_node is not None):
        if node_counter == N-k-1:
            n_m_k_m_1_pointer = this_node
            print("N-k-1: {}".format(n_m_k_m_1_pointer))
        elif node_counter == N-k:
            n_m_k_pointer = this_node
            print("N-k: {}".format(n_m_k_pointer))
        elif node_counter == N-k+1:
            n_m_k_p_1_pointer = this_node
            print("N-k+1: {}".format(n_m_k_p_1_pointer))
        
        # take the next step in the list
        this_node = this_node.next
        node_counter += 1
    
    if (N > 1) and (k != N-k):
        # Now swap the pointers to change the order
        if k_m_1_pointer:
            k_m_1_pointer.next = n_m_k_pointer
        n_m_k_pointer.next = k_p_1_pointer
        n_m_k_m_1_pointer.next = k_pointer
        k_pointer.next = n_m_k_p_1_pointer

    return linked_list


if __name__ == "__main__":
    node1 = Node(data=1)
    node2 = Node(data=2)
    node3 = Node(data=3)
    node4 = Node(data=4)
    node5 = Node(data=5)
    
    this_list = Linked_list(node1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print_list(this_list)

    swapped_list = swap_k_and_n_m_k(this_list, 2)

    print_list(swapped_list)
