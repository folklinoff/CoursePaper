package params

import (
	"fmt"
)

func MultipleItemsParams(limit *string, currentPage *string) string {
	newLimit := "limit"
	if limit != nil {
		newLimit = *limit
	}
	newPage := "currentPage"
	if currentPage != nil {
		newPage = *currentPage
	}
	return fmt.Sprintf(`js:{limit:%s, currentPage:%s}`, newLimit, newPage)
}
