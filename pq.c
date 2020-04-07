// priority_queue.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct List {
  struct List *prev, *next; 
  char *data; 
}; 

void init_head(struct List *head){
  head->next = head->prev = head; 
} //(*head).next = head;
  //(*head).prev = head;

int is_empty(struct List *head) {
  return head->next == head;
}

void add_to_last(struct List *head, struct List *list) {
    list->next = head; //list's next is now pointing to the head address.
    //TODO - Complete setting up links to insert this node (list)
    //list->prev = head->prev->prev->next;
    // head->prev->next = list;
    // head->prev = list;
    // // prior to the head node (head)
    list->prev = head->prev;
    head->prev->next = list;
    head->prev = list;
    
}

void add_to_first(struct List *head, struct List *list) { //Adding a node between head and the seond node
    list->next = head->next;
    list->prev = head;
    head->next->prev = list;
    head->next = list;
}

void add_after(struct List *thisOne, struct List *list) { //
  list->next = thisOne->next;
  list->prev = thisOne;
  thisOne->next->prev = list;
  thisOne->next = list;
}

struct List* remove_last(struct List *head) {
  struct List *list = head->prev; //list Node = head's prev
  head->prev->prev->next = head;
  //TODO - Fix links to remove the last node in the list.
  head->prev = head->prev->prev;
  list->next = list->prev = NULL;

  //  This is the node immediately before head
  return list;  //  The method will return the node that was removed
}

struct List* remove_first(struct List *head) {
  //TODO
  struct List *list = head->next;
  head->next->next->prev = head; // point element 2 to head
  head->next = head->next->next; // point head next to element 2
  list->next = list->prev = NULL; // null out points in removed node
  return list;
}

struct List free_list[500];
struct List free_head;

void init_free_list() {
  int i;
  init_head(&free_head);
  for(i = 0; i < 500; i++)         //link the 500 free lists
    add_to_last(&free_head, free_list + i);
}

struct List *new_list() {            //get a new List struct
  if(is_empty(&free_head)) {
    printf("out of list\n");
    exit(0);
  }
  return remove_first(&free_head); //queue
}

void del_list(struct List *list) {  //free a List struct
  add_to_first(&free_head, list);  //queue
}

// Compares the data in two list nodes.
// Returns: -1 if list1 data is less than list2 data
//          1 if list1 data is greater than list2 data
//          0 if data fields are equivalent
int compare(struct List *list1, struct List *list2) {
  //TODO - write code to compare the words and return
  //  -1 if list1->data is less (english sorting order) than list2->data
  //  0 if the two words are identical in content
  // 1 if list1->data is greater than (sorts after) list2->data
  // Hint, look at string functions in the c library that may help
  if(strcmp(list1->data, list2->data) < 0 ){
      return -1;
   }
   else if(strcmp(list1->data, list2->data) == 0){
      return 0;
   }
   else if(strcmp(list1->data, list2->data) > 0){
      return 1;
   }
}

// insert - This function inserts the element list into
//         the linked list pointed at by head. It places the
//         node where the data should sort.
//            i.e. If the list is:
//
//          head-> node('a') -> node ('l') -> node ('n') -> head
//
//         and we insert a list node with the letter 'd', the new
//         list should be:
//
//          head-> node('a') -> mode ('d') -> node ('l') -> node ('n') -> head
//
void insert(struct List *head, struct List *list) {
  struct List *theNext = head->next;
  int inserted = 0;
  // Check if it is before first element add_to_first()
  if (is_empty(head) || (compare(list, theNext) == -1)) { //if list is less than theNext.
    add_to_first(head, list);
    return;
  }
  // Loop and wait till it is larger than theNext. Insert after theNext->prev
  while (theNext != head) {
    int cres = compare(list, theNext);
    if (cres <= 0) {
      add_after(theNext->prev, list);
      return;
    } else {
      theNext = theNext->next;
    }      
  }

  // insert at end (add_to_last)
  add_to_last(head, list);
}

void print_list(struct List *lhead) {
  struct List *node;
  int nodes_printed = 0;
  printf("Printing:\n");
  printf("lhead: %p, n:%p, p:%p\n", lhead, lhead->next, lhead->prev);
  //  while ((node != lhead) || (nodes_printed == 0)) {
  for (node = lhead->next; node != lhead; node = node->next) {
    nodes_printed++;
    printf("%s \n", node->data);
  }
  printf("\n");
}

void print_list_data(struct List *lhead) {
  struct List *node;
  int nodes_printed = 0;
  printf("Printing:\n");
  printf("lhead: %p, n:%p, p:%p\n", lhead, lhead->next, lhead->prev);
  //  while ((node != lhead) || (nodes_printed == 0)) {
  for (node = lhead->next; node != lhead; node = node->next) {
    nodes_printed++;
    printf("%s \n", node->data);
  }
  printf("\n");
}

int list_count_elements(struct List *head) {
    // TODO  - write a method to step through the list and return the number of nodes.
    int count = 0;
    struct List* counter = head->next;
    while(counter != head){ //keep moving until it reaches the HEAD address
        counter = counter -> next;
        count++;
    }
    //printf("%d\n",count);
    return count;
}

//
// alphabetize - Takes the words in the string (str) and alphabetizes them
// using a priority queue implemented on a linked list.
//
char **alphabetize(char *str) {
  struct List pq;
  int i;
  char *sep = " ";
  char *rest;
  char *token;
  char *word;
  char **wordlist;
  int wordcount;
  //printf("str is : %s\n", str);
  init_head(&pq);
  // Extract words and add them to the pq
  rest = str;
  
  // token = strtok_r(rest, sep, &rest);
  // printf("%s\n", token);
  while ((token = strtok_r(rest, sep, &rest))) {
    //printf("pass");
    struct List *list = new_list();  // Build a new list node
    // TODO: Copy the next word (token) to the data field in the node
    //    and add the node to the priority queue with insert()
    list->data = token;
    //printf("pass2");
    insert(&pq, list);
  }
  //printf("pass3");
  wordcount = list_count_elements(&pq);
  wordlist = (char **)malloc((wordcount+1) * sizeof(char *));

  for(i = 0; !is_empty(&pq); i++) {
    struct List *list;
    //printf("%s\n", &pq);
    //TODO: pop list from stack and update wordlist[i] with that word
    list = remove_first(&pq); 
    wordlist[i] = list->data;
    // TODO: 'Free' the node removed from the list
    del_list(list);
    //free(list);

  }
  wordlist[wordcount] = 0; // null the last slot
  return wordlist;
}

void print_words(char **wordList) {
  // TODO write code to print each word in the array
  // of strings passed in
  //printf("the length of wordList is: %d\n", strlen(wordList[0])); //why is this only four?
  int index = 0;
  int check = 0;

  while(check == 0){
      if(wordList[index] != 0){
          printf("%s\n", wordList[index]);
          index = index + 1;
      }
      else{
          break;
      }
  }  
}


int main() {
  char *str;
  size_t bufsize;
  int ccount;
  char **theList;
  str = (char *) malloc(100);
  bufsize = 100;
  init_free_list();

  // Prompt user and read a sentence
  printf("enter a sentence: ");
  ccount = getline(&str, &bufsize, stdin);
  str[ccount-1] = 0; // remove newline 
  printf("sentence is: %s\n", str);
  printf("sorted words: \n");
  theList = alphabetize(str);
  
  print_words(theList);
}
      