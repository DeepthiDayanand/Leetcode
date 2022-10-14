/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        
        if (head->next == nullptr)
            return nullptr;
        
        int length = 0;
        ListNode *x = head, *y = head;
        
        //Counting nodes in linked list
        while (x != nullptr) {
             length++;
             x = x->next;   
        }
           
        int mid = length/2;
        
        for ( int i = 0; i < mid - 1; i++)
            y = y->next;
        
        y -> next = y->next->next;
        return head;   
            
    }
};