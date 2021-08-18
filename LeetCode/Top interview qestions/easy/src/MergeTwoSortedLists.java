public class MergeTwoSortedLists {

    public static class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }

    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {

          ListNode answer = null;
          ListNode node1 = l1;
          ListNode node2 = l2;

        ListNode temp = null;
        while (node1!=null && node2!=null){

            if(node1.val <= node2.val){
                if(answer == null){
                    answer = new ListNode(node1.val);
                    temp = answer;
                }else{
                    answer.next = new ListNode(node1.val);
                    answer = answer.next;
                }
                node1 = node1.next;

            }else{
                System.out.println(node2.val);
                if(answer == null){
                    answer = new ListNode(node2.val);
                    temp = answer;
                }else{
                    answer.next = new ListNode(node2.val);
                    answer = answer.next;
                }
                node2 = node2.next;
            }
        }

        if(node1 != null){
            while(node1 != null){
                if(answer == null){
                    answer = new ListNode(node1.val);
                    temp = answer;
                }else{
                    answer.next = new ListNode(node1.val);
                    answer = answer.next;
                }

                node1 = node1.next;
            }
        }



        if(node2 != null){
            while(node2 != null){
                if(answer == null){
                    answer = new ListNode(node2.val);
                    temp = answer;
                }else{
                    answer.next = new ListNode(node2.val);
                    answer = answer.next;
                }
                node2 = node2.next;
            }
        }

        return temp;

    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(1, new ListNode(2, new ListNode(4)));
        ListNode l2 = new ListNode(1, new ListNode(3, new ListNode(4)));
        ListNode ans = mergeTwoLists(l1, l2);
        while(ans!=null){
            System.out.println(">> "+ans.val) ;
            ans = ans.next;
        }


    }

}

