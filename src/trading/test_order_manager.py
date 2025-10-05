import unittest
from unittest.mock import patch, MagicMock
from src.trading.order_manager import OrderManager

class TestOrderManagerInit(unittest.TestCase):
    @patch('src.trading.order_manager.get_logger')
    @patch('src.trading.order_manager.BrokerInterface')
    def test_init_live_true(self, mock_broker, mock_logger):
        om = OrderManager(live=True, broker_api_key='key', broker_secret='secret')
        mock_logger.assert_called_with("OrderManager")
        mock_broker.assert_called_with('key', 'secret')
        self.assertTrue(om.live)
        self.assertEqual(om.logger, mock_logger.return_value)
        self.assertEqual(om.broker, mock_broker.return_value)

    @patch('src.trading.order_manager.get_logger')
    def test_init_live_false(self, mock_logger):
        om = OrderManager(live=False)
        mock_logger.assert_called_with("OrderManager")
        self.assertFalse(om.live)
        self.assertEqual(om.logger, mock_logger.return_value)
        self.assertIsNone(om.broker)

        class TestOrderManagerExecute(unittest.TestCase):
            @patch('src.trading.order_manager.get_logger')
            @patch('src.trading.order_manager.BrokerInterface')
            def test_execute_live_true_success(self, mock_broker, mock_logger):
                om = OrderManager(live=True, broker_api_key='key', broker_secret='secret')
                mock_broker_instance = mock_broker.return_value
                mock_broker_instance.execute_order.return_value = True

                mock_portfolio = MagicMock()
                signal = {'asset': 'AAPL', 'action': 'BUY', 'size': 10, 'price': 150}

                om.execute(signal, mock_portfolio)

                mock_broker_instance.execute_order.assert_called_once_with('AAPL', 'BUY', 10, 150)
                mock_portfolio.add_position.assert_called_once_with('AAPL', 10, 150)

            @patch('src.trading.order_manager.get_logger')
            @patch('src.trading.order_manager.BrokerInterface')
            def test_execute_live_true_failure(self, mock_broker, mock_logger):
                om = OrderManager(live=True, broker_api_key='key', broker_secret='secret')
                mock_broker_instance = mock_broker.return_value
                mock_broker_instance.execute_order.return_value = False

                mock_portfolio = MagicMock()
                signal = {'asset': 'AAPL', 'action': 'SELL', 'size': 5, 'price': 140}

                om.execute(signal, mock_portfolio)

                mock_broker_instance.execute_order.assert_called_once_with('AAPL', 'SELL', 5, 140)
                mock_portfolio.add_position.assert_not_called()

            @patch('src.trading.order_manager.get_logger')
            def test_execute_live_false(self, mock_logger):
                om = OrderManager(live=False)
                mock_portfolio = MagicMock()
                signal = {'asset': 'GOOG', 'action': 'BUY', 'size': 2, 'price': 2800}

                om.execute(signal, mock_portfolio)

                mock_logger.return_value.info.assert_called_once_with(
                    "[PAPER] Executing BUY GOOG size 2 at 2800"
                )
                mock_portfolio.add_position.assert_called_once_with('GOOG', 2, 2800)

if __name__ == '__main__':
    unittest.main()