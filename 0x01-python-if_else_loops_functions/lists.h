#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s
 * @k: integer
 * @next: pointer to the next node
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int k;
	struct listint_s *next;
}listint_t;

size_t print_listint(const litint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int k);
void free_listint(list_t *head);
listint_t *insert_node(listint_t **head, int number);

#endif
