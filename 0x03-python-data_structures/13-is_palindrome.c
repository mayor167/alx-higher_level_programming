#include "lists.h"

/**
 * reversed_list - program to reverse a linked list
 * @head: pointer to first node
 *
 * Return: pointer first node in the list
 */
void reversed_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - prog to check if linked list is palindrome
 * @head: pointer to linked list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *quick = *head, *notQuick = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		quick = quick->next->next;
		if (!quick)
		{
			dup = notQuick->next;
			break;
		}
		if (!quick->next)
		{
			dup = notQuick->next->next;
			break;
		}
		notQuick = notQuick->next;
	}

	reversed_list(&dup);

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
