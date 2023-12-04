#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * add_nodeint - adds a new node
 * @head: head 
 * @n: int to add 
 * Return: address of the new, or NULL if it failed
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *nw;

	nw = malloc(sizeof(listint_t));
	if (nw == NULL)
		return (NULL);
	nw->n = n;
	nw->next = *head;
	*head = nw;
	return (nw);
}

/**
 * is_palindrome - id linked list is palindrome
 * @head: head 
 * Return: 1 it is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *head2 = *head;
	
	listint_t *x = NULL, *y = NULL;
	if (*head == NULL || head2->next == NULL)
		return (1);
	while (head2 != NULL)
	{
		add_nodeint(&x, head2->n);
		head2 = head2->next;
	}
	y = x;
	while (*head != NULL)
	{
		if ((*head)->n != y->n)
		{
			free_listint(x);
			return (0);
		}
		*head = (*head)->next;
		y = y->next;
	}
	free_listint(x);
	return (1);
}
