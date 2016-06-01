"""Tasks for OperationContainer plugin integration tests."""


def find_trading_fees_for_positions(container):
    """Finds the fees for all positions in the container."""
    if 'positions' in container.context:
        for position_type, position_value in container.context['positions'].items():
            for position in position_value.values():
                if position.operations:
                    for operation in position.operations:
                        operation.commissions.update(
                            container.trading_fees.get_fees(
                                operation, position_type
                            )
                        )
                else:
                    position.commissions.update(
                        container.trading_fees.get_fees(
                            position, position_type
                        )
                    )
