def compute_instantaneous_inflation(pi_series, alpha):
    """Beregn π_t^{12,α} = (∏_{k=0}^{11} (1 + π_{t-k})^{κ(k,α)}) - 1"""
    def instant_inflation_at_t(window):
        if len(window) < 12 or window.isna().any():
            return np.nan
        
        product = 1.0
        for k in range(12):
            kappa = compute_kappa(k, alpha)
            pi_t_minus_k = window.iloc[-(k+1)]  # Nyeste er i slutningen
            product *= (1 + pi_t_minus_k)**kappa
        
        return product - 1
    
    return pi_series.rolling(window=12).apply(instant_inflation_at_t, raw=False)