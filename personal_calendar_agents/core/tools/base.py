class Tool:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError
    def __repr__(self):
        return self.__doc__ or ""