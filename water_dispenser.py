class WaterDispenser:
    def __init__(self, capacity=20):
        self.capacity = capacity  # Capacidad del bidón en litros
        self.current_level = capacity  # Nivel actual del agua
        self.cold_temp = 10  # Temperatura mínima del agua fría
        self.hot_temp = 90  # Temperatura máxima del agua caliente
        self.ambient_temp = 25  # Temperatura ambiente
        self.current_cold_temp = 25  # Inicialmente no está frío
        self.current_hot_temp = 25  # Inicialmente no está caliente

    def dispense(self, mode, amount):
        if self.current_level < amount:
            return "Agua insuficiente, reponer bidón"
        
        if mode == "fría" and self.current_cold_temp > self.cold_temp:
            return "El agua no está suficientemente fría"
        
        if mode == "caliente" and self.current_hot_temp < self.hot_temp:
            return "El agua no está suficientemente caliente"
        
        self.current_level -= amount
        return f"Dispensando {amount} litros de agua {mode}"
    
    def refill(self):
        self.current_level = self.capacity
        return "Bidón de agua reemplazado"
    
    def set_cold_temp(self, temp):
        self.current_cold_temp = temp
    
    def set_hot_temp(self, temp):
        self.current_hot_temp = temp