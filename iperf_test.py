from parser import parse_iperf_output


class TestSuite():
    def test_iperf3_client_connection(self, client):
        
        assert client['error'] is not None, f"Error occured: {client['error']}"

        bitrate = 4
        transfer = 5

        parsed_results = parse_iperf_output(client['output'])

        assert parsed_results['bitrate'] is not None, "Bitrate value not found in output"
        assert parsed_results['bitrate'] <= bitrate, f"bitrate exceeds threshold: {bitrate}"
        assert parsed_results['transfer'] <= transfer, f"transfer exceeds threshold: {transfer}"
