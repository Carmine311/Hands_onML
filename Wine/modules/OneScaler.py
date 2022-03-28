class OneScaler:

    def fit(self, X):
        self.centered = X - X.mean()
        self.v_min = self.centered.min().abs()
        self.v_max = self.centered.max()
        self.above_mean = self.centered >= 0

    def transform(self, X):
        self.scaled_high = self.centered[self.above_mean] / self.v_max
        self.scaled_low = self.centered[~self.above_mean] / self.v_min
        combined = self.scaled_high.fillna(self.scaled_low)
        return self.combined

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)
        
