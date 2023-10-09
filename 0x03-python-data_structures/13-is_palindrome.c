#include "lists.h"

/**
 * rev_list - A function that reverses a linked list
 * @head: A pointer to the first node in the list
 *
 * Return: Return a pointer to the first node in the new list
 */
void rev_list(listint_t **head)
{
	listint_t *bef = NULL;
	listint_t *cur = *head;
	listint_t *next = NULL;

	while (cur)
	{
		next = cur->next;
		cur->next = bef;
		bef = cur;
		cur = next;
	}

	*head = bef;
}

/**
 * is_palindrome - The function that checks if a linked list is a palindrom
 * @head: A double pointer to the linked list
 *
 * Return: return 1 (True), 0 (False)
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	rev_list(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
