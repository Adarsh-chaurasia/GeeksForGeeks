def sortedMerge(head1, head2):
    if head1.data<head2.data:
        startM=head1
        head1=head1.next
    else:
        startM=head2
        head2=head2.next
        
    pM=startM
    
    while head1 and head2:
        if head1.data<head2.data:
            pM.next=head1
            pM=pM.next
            head1=head1.next
            
            
        else:
            pM.next=head2
            
            pM=pM.next
            head2=head2.next
        
        
    if head1:
        pM.next=head1
            
    else:
        pM.next=head2
            
    return startM
