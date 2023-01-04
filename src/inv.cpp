#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/eigen.h>
#include <boost/smart_ptr/shared_ptr.hpp>
#include <boost/random.hpp>
#include <boost/random/random_device.hpp>
//#include <xtensor>
#include <Eigen/LU>
#include <Eigen/Dense>

namespace py = pybind11;

using namespace pybind11::literals;
using namespace std;

#define EIGEN_USE_MKL_ALL

Eigen::MatrixXd inv(Eigen::MatrixXd& xs) {
    return xs.inverse();
}

Eigen::VectorXd lstsq(Eigen::MatrixXd& A, Eigen::VectorXd& b) {
    return (A.transpose() * A).ldlt().solve(A.transpose() * b);
}

double logn(double mu, double sigma){
    boost::random::mt19937 engine; // uniform random bit engine
    // seed the URBG
    boost::random::random_device dev;
    engine.seed(dev); // actually without call operator is better with boost

    // setup a distribution:
    // double mu    = 1.0;
    // double sigma = 1.0;
    return boost::random::lognormal_distribution<double> dist(mu, sigma);
}


boost::shared_ptr<int> p1{new int{1}};
//xt::xarray<double> a = xt::random::randn<double>({10}, -0.5, 0.5);



PYBIND11_PLUGIN(inv) {
    pybind11::module m("code", "auto-compiled c++ extension");
    m.def("inv", &inv);
    m.def("lstsq", &lstsq);
    m.def("logn", &logn);
    return m.ptr();
}