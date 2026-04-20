    def test_delete_car(self):
        """Test deleting car"""
        # Create car
        car = self.controller.create_car(
            car_code="XE001",
            brand="Toyota",
            model="Camry",
            year=2023,
            price=1200000000.0
        )
        
        # Delete car
        result = self.controller.delete_car(car.id)
        assert result is True
        
        # Verify car is deleted
        deleted_car = self.controller.get_car_by_id(car.id)
        assert deleted_car is None