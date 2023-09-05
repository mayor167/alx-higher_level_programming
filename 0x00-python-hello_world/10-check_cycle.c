#include "lists.h"
#include <stdlib.h>
/**
 * check_cycle -function Checks if a singly-linked list contains a cycle.
 * @list: A pointer linked list.
 *
 * Return: 0 if no cycle.
 *         1 if cylce dey.
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
