package tools

func T[T any](val T) *T {
	return &val
}
