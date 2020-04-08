class Solution {
    fun middleNode(head: ListNode?): ListNode? {
        // Given a non-empty, singly linked list with head node head, return a
        // middle node of linked list.
        //
        // If there are two middle nodes, return the second middle node.
        var slow = head;
        var fast = head;

        while (fast?.next != null) {
            slow = slow?.next;
            fast = fast?.next?.next;
        }

        return slow;
    }
}
