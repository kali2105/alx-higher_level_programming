#include "lists.h"

/**
 * check_cycle - A function that checks if a linked list contains a cycle
 * @list: linked list to be checked
 *
 * Return: 1 (Cycle is detected) OR 0 (NOT detected)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
	if (!list)
	{
	return (0);
	}
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

	if (fast == slow)
	{
		return (1);
	}
	}
	return (0);
}
