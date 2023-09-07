#include "lists.h"


/**
 * insert_node - func to insert node into an ordered list
 * @head: pointer to the head of the list
 * @number: value to insert
 * Return: pointer to the inserted node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nPosition = *head, *added;

	added = malloc(sizeof(listint_t));
	if (added == NULL)
	{
		return (NULL);
	}
	added->n = number;

	if (nPosition == NULL || number < nPosition->n)
	{
		added->next = nPosition;
		*head = added;
		return (added);
	}

	while (nPosition && nPosition->next && nPosition->next->n < number)
	{
		nPosition = nPosition->next;
	}

	added->next = nPosition->next;
	nPosition->next = added;

	return (added);
}
