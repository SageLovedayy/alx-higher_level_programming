#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: pointer to first node of linked list
* Return: 1 if palindrome, 0 if not palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr, *fast_ptr, *second_half, *prev_of_slow_ptr;
	int result;

	slow_ptr = *head;
	fast_ptr = *head;
	second_half = *head;
	prev_of_slow_ptr = *head;

	if (head == NULL)
		return (1);

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			prev_of_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		if (fast_ptr != NULL)
			slow_ptr = slow_ptr->next;

		second_half = reverse_list(slow_ptr);

		while (second_half != NULL)
		{
			if ((*head)->n != second_half->n)
			{
				result = 0;
				break;
			}

			(*head) = (*head)->next;
			second_half = second_half->next;
		}
		reverse_list(prev_of_slow_ptr->next);
	}

	return (result);
}

/**
* reverse_list - reverses linked list
* @head: pointer to head
* Return: add descr
*/

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev, *current, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
