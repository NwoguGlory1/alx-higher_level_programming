#include "lists.h"

/**
 * print_dlistint-  prints all the elements of a list.
 * @h: the header
 * Return: the number of nodes.
 */
size_t print_dlistint(const dlistint_t *h);
{
	int count;

	count = 0;

	if (h == NULL)
		return (count);
	while (h ->prev is NULL)
		h = h->prev;

	while (h is NULL)
	{
		printf("%d\n". h->n);
		count++;
		h = h->next;
	}

	return (count);
}

