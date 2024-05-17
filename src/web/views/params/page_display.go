package params

import (
	"fmt"
	"net/url"
	"reflect"
	"strconv"
	"strings"
)

type PageDisplayParams struct {
	Limit       int `url_param:"limit,default=20"`
	CurrentPage int `url_param:"currentPage,default=1"`
}

func GetPageDisplayParams(params url.Values) (*PageDisplayParams, error) {
	p := &PageDisplayParams{}
	t := reflect.TypeOf(p).Elem()
	v := reflect.ValueOf(p).Elem()
	for i := range t.NumField() {
		field := t.Field(i)
		val, err := GetParamFieldValue(params, field)
		if err != nil {
			return nil, err
		}
		v.Field(i).Set(reflect.ValueOf(val))
	}
	return p, nil
}

func GetParamFieldValue(params url.Values, t reflect.StructField) (any, error) {
	s, ok := t.Tag.Lookup("url_param")
	if !ok {
		return reflect.Value{}, fmt.Errorf("url_param tag required")
	}
	switch t.Type.Kind() {
	case reflect.Int:
		return GetParamFieldInt(params, s)
	}
	return reflect.Value{}, nil
}

func GetParamFieldInt(params url.Values, tagValue string) (int, error) {
	options := strings.Split(tagValue, ",")
	var stringVal string
	if params.Has(options[0]) {
		stringVal = params.Get(options[0])
	} else {
		for _, opt := range options {
			if strings.HasPrefix(opt, "default=") {
				stringVal, _ = strings.CutPrefix(opt, "default=")
			}
		}
	}
	intVal, err := strconv.ParseInt(stringVal, 10, 0)
	if err != nil {
		return 0, err
	}
	return int(intVal), nil
}
