#include "lists.h"

/**
 * insert_node - Inserts a new node with a given number into
 * a sorted singly linked list.
 *
 * @head: Pointer to the head of the linked list.
 * @number: Number to insert.
 * Return: On success, pointer to the new node; on failure, NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	/* If the linked list is empty or new node should be inserted at beginning*/
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head; /*Set the next of the new node to the current head*/
		*head = new_node;	/* Update the head to point to the new node*/
		return (new_node);
	}

	/* Traversal to find the appropriate position for the new node*/
	current = *head;
	while (current->next && current->next->n < number)
		current = current->next;

	/* Insertion */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
