package handler

import "github.com/labstack/echo/v4"

func RedirectWithQueryParams(next echo.HandlerFunc) echo.HandlerFunc {
	return func(c echo.Context) error {
		if !c.QueryParams().Has("limit") {
			c.QueryParams().Add("limit", "20")
		}
		if !c.QueryParams().Has("offset") {
			c.QueryParams().Add("offset", "0")
		}
		return next(c)
	}
}
