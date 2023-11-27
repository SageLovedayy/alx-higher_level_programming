#include "lists.h"

/**
* check_cycle - checks if linked list has cycle
* @list: linked list
* Return: 1 if cycle found, 0 if no cycle found
*/
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (fast == slow)
		{

			return (1); /*cycle found*/
		}

		slow = slow->next;
		fast = fast->next->next;
	}



	return (0);
}
