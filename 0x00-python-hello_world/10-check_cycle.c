#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle -function Checks if a singly-linked list contains a cycle.
 * @list: A pointer singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortle, *haire;

	if (list == NULL || list->next == NULL)
		return (0);

	tortle = list->next;
	haire = list->next->next;

	while (tortle && haire && haire->next)
	{
		if (tortle == haire)
			return (1);

		tortle = tortle->next;
		haire = haire->next->next;
	}

	return (0);
}
