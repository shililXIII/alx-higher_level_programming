#include "lists.h"
/**
 * check_cycle - found the cycle
 * @list: pointer
 * Return: 0 no cycle 1 to a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *x, *y;

	if (list == NULL || list->next == NULL)
		return (0);
	x = list;
	y = x->next;
	while (x != NULL && y->next != NULL && y->next->next != NULL)
	{
		if (x == y)
			return (1);
		x = x->next;
		y = y->next->next;
	}
	return (0);
}
