#include <stdio.h>
#include <stdlib.h>

typedef struct listNode{
    int Data;
    struct listNode* Next;
    struct listNode* Prev;
}Node;

// node creation
Node* createNode(int data){
    Node* newNode = (Node*)malloc(sizeof(Node));

    // variable initialization
    newNode -> Data = data;
    newNode -> Next = NULL;
    newNode -> Next = NULL;

    return newNode;
}

void deleteNode(Node* Node){
    free(Node);
}

Node* getNodeAt(Node* head, int index){
    Node* horse = head;
    int count = 0;
    while(horse != NULL){
        if(count++ == index){
            return horse;
        } 
        horse = horse -> Next;
    }
    return NULL;
}

int countNode(Node* head){
    int count = 0;
    Node* horse = head;
    while(horse != NULL){
        horse=horse -> Next;
        count++;
    }
    return count; 
}

void addNode(Node** head, Node* newNode){
    // no list exists
    if((*head)==NULL){
        *head = newNode;
    }
    else{
        Node* horse = *head;
        while(horse -> Next != NULL){
            horse = horse -> Next;
        }
        horse -> Next = newNode;
        newNode -> Prev = horse;
    }
}
void inserAfter(Node* Current, Node* newNode){
    //head
    if(Current -> Prev == NULL && Current -> Next == NULL){
        Current -> Next = newNode;
        newNode -> Prev = Current;
    }

    //Not head

        // if tai;
        if(Current -> Next == NULL){
            Current -> Next = newNode;
            newNode -> Prev = Current;
        }
        else{
            Current -> Next -> Prev = newNode; //커렌트의 넥스트의 프레브가 뉴 노드
            newNode -> Prev = Current;
            newNode -> Next = Current -> Next;
            Current -> Next = newNode;
        }
        // in the middle of 2 nodes
}

void removeNode(Node** head, Node* remove){
    // when head
    if(*head == remove){
        *head = remove -> Next;
    }
    //when remove has some node to go
    if(remove->Next != NULL){
        remove -> Next -> Prev = remove -> Prev;
    }
    //when remove has prev link to go
    if(remove->Prev != NULL){
        remove -> Prev -> Next = remove -> Next;
    }

    deleteNode(remove);
}